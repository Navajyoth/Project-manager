(function(){
  angular.module('app')
    .filter('statusFilter', statusFilter)
    .controller('ProjectCtrl', ProjectCtrl)
    .controller('addTaskModalCtrl', addTaskModalCtrl);

  ProjectCtrl.$inject = ['$scope', '$stateParams', '$state', 'Tasks', 'commonSrv', 'toastr', 'tasks','$modal'];

  function ProjectCtrl($scope, $stateParams, $state, Tasks, commonSrv, toastr, tasks,$modal){
    var vm = this;

    init();
   
    console.log(tasks);
    function init(){
      vm.statusOptions = ['backlog', 'progress', 'rework', 'review', 'complete'];
      vm.tasks = tasks;
    }


  $scope.projectId =$stateParams.projectId;
  vm.addTaskModal = function () {
  var addTaskModal = $modal.open({
      animation: true,
      templateUrl: '/static/apps/projects/html/modal.addtask.html',
      controller:'addTaskModalCtrl',
      scope:$scope
    });

 // function for handling success full exit of modal
  addTaskModal.result.then(function (task){
    vm.tasks.push(task);
  });

  }

 
}


addTaskModalCtrl.$inject = ['$scope','Tasks','$modalInstance','commonSrv'];
function addTaskModalCtrl($scope,Tasks,$modalInstance,commonSrv){
   $scope.addTask = function (newTask) {
        newTask.project=$scope.projectId;
        var task = new Tasks(newTask);

        task.$save(function(task){
          $modalInstance.close(task); // this argument can be received from modalinstance.result.then function 
        }, commonSrv.handleError);
        

  }

}

  function statusFilter(){
    return function(tasks, status){
      return _.filter(tasks, function(task){
        return task.status===status;
      });
    }
  }
})();



