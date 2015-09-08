(function(){
  angular.module('app')
    .filter('taskUserFilter', taskUserFilter)
    .controller('UsersTasksCtrl', UsersTasksCtrl)
    .controller('UserTasksCtrl', UserTasksCtrl);

  UserTasksCtrl.$inject = ['$scope', '$stateParams', '$state', 'Tasks', 'commonSrv', 'toastr'];
  UsersTasksCtrl.$inject = ['$scope', '$stateParams', '$state', 'Tasks', 'Users', 'commonSrv', 'toastr', '$timeout'];

  function UserTasksCtrl($scope, $stateParams, $state, Tasks, commonSrv, toastr){
    var vm = this;

    init();

    function init(){
      vm.statusOptions = ['backlog', 'progress', 'rework', 'review', 'complete'];
      vm.tasks = Tasks.user({userId:$stateParams.userId});
    }
  }

  function UsersTasksCtrl($scope, $stateParams, $state, Tasks, Users, commonSrv, toastr, $timeout){
    var vm = this;
    var dragTask;

    init();
    function init(){
      vm.users = Users.query();
      vm.tasks = Tasks.query({status:'backlog,progress,rework', detail:true});
    }

    //for changing/assigning user on a task
    vm.setUser = function (user,task,oldTaks) {
      var index = vm.tasks.indexOf(oldTaks);
                  vm.tasks.splice(index,1);
      // To tackle dropping on the same place
      if(task.user==user.id){
        return;
      }
      task.user = user.id?user.id:null;
      var Task = new Tasks(task);
      Task.$update(function(){
        var msg = user.id?'Task ' + task.title + ' assigned to ' + user.name:'Task ' + task.title + ' has been  unassigned ';
        toastr.success(msg);
      }, commonSrv.handleError);
    }

    vm.drapOptions = {
      accept: function(dragEl) {
        console.log(123);
        if ($scope.list1.length >= 2) {
          return false;
        } else {
          return true;
        }
      }
    }; 

  }

  function taskUserFilter(){
    return function(tasks, userId){
      return _.filter(tasks, function(task){
        return task.user==userId;
      });
    }
  }

})();


