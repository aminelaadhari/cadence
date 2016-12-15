package workflow

import (
	"fmt"
	"os"
	"testing"
	"time"

	log "github.com/Sirupsen/logrus"
	"github.com/stretchr/testify/suite"
	"github.com/uber-common/bark"

	workflow "code.uber.internal/devexp/minions/.gen/go/shared"
	"code.uber.internal/devexp/minions/common"
	"code.uber.internal/devexp/minions/persistence"
)

type (
	transferQueueProcessorSuite struct {
		suite.Suite
		TestBase
		processor *transferQueueProcessorImpl
	}
)

func TestTransferQueueProcessorSuite(t *testing.T) {
	s := new(transferQueueProcessorSuite)
	suite.Run(t, s)
}

func (s *transferQueueProcessorSuite) SetupSuite() {
	if testing.Verbose() {
		log.SetOutput(os.Stdout)
	}

	s.SetupWorkflowStore()
	s.processor = newTransferQueueProcessor(s.WorkflowMgr, s.TaskMgr,
		bark.NewLoggerFromLogrus(log.New())).(*transferQueueProcessorImpl)
}

func (s *transferQueueProcessorSuite) TearDownSuite() {
	s.TearDownWorkflowStore()
}

func (s *transferQueueProcessorSuite) TestNoTransferTask() {
	// First cleanup transfer tasks from other tests
	s.ClearTransferQueue()

	newPollInterval := s.processor.processTransferTasks(transferProcessorMinPollInterval)
	s.Equal(2*transferProcessorMinPollInterval, newPollInterval)
}

func (s *transferQueueProcessorSuite) TestSingleDecisionTask() {
	// First cleanup transfer tasks from other tests
	s.ClearTransferQueue()

	workflowExecution := workflow.WorkflowExecution{WorkflowId: common.StringPtr("single-decisiontask-test"),
		RunId: common.StringPtr("0d00698f-08e1-4d36-a3e2-3bf109f5d2d6")}
	taskList := "single-decisiontask-queue"
	task0, err0 := s.CreateWorkflowExecution(workflowExecution, taskList, "decisiontask-scheduled", nil, 3, 0, 2)
	s.Nil(err0, "No error expected.")
	s.NotEmpty(task0, "Expected non empty task identifier.")

	newPollInterval := s.processor.processTransferTasks(time.Second)
	s.Equal(transferProcessorMinPollInterval, newPollInterval)

	tasks1, err1 := s.GetTasks(taskList, persistence.TaskTypeDecision, time.Second, 1)
	s.Nil(err1)
	s.NotEmpty(tasks1)
	s.Equal(1, len(tasks1))

	dTask := tasks1[0]
	s.Equal(int64(2), dTask.ScheduleID)
}

func (s *transferQueueProcessorSuite) TestManyTransferTasks() {
	// First cleanup transfer tasks from other tests
	s.ClearTransferQueue()

	workflowExecution := workflow.WorkflowExecution{WorkflowId: common.StringPtr("many-transfertasks-test"),
		RunId: common.StringPtr("57d5f005-bdaa-42a5-a1c5-b9c45d8699a9")}
	taskList := "many-transfertasks-queue"
	activityTaskScheduleIds := []int64{2, 3, 4, 5, 6}
	task0, err0 := s.CreateWorkflowExecutionManyTasks(workflowExecution, taskList, "t1;t2;t3;t4;t5", nil, 7, 0, nil,
		activityTaskScheduleIds)
	s.Nil(err0, "No error expected.")
	s.NotEmpty(task0, "Expected non empty task identifier.")

	newPollInterval := s.processor.processTransferTasks(time.Second)
	s.Equal(transferProcessorMinPollInterval, newPollInterval)

	tasks1, err1 := s.GetTasks(taskList, persistence.TaskTypeActivity, time.Second, 10)
	s.Nil(err1)
	s.NotEmpty(tasks1)
	s.Equal(len(activityTaskScheduleIds), len(tasks1))

	for _, t := range tasks1 {
		s.True(containsID(activityTaskScheduleIds, t.ScheduleID),
			fmt.Sprintf("ScheduleID: %v, TaskList: %v", string(t.ScheduleID), t.TaskList))
		s.Equal(workflowExecution.GetWorkflowId(), t.WorkflowID)
		s.Equal(workflowExecution.GetRunId(), t.RunID)
		s.Equal(taskList, t.TaskList)
		s.Equal(1, t.DeliveryCount)
		s.Equal(persistence.TaskTypeActivity, t.TaskType)
	}
}

func containsID(list []int64, scheduleID int64) bool {
	for _, id := range list {
		if id == scheduleID {
			return true
		}
	}

	return false
}