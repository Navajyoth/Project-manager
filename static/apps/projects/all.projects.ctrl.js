(function(){
  angular.module('app')
  .controller('AllProjectsCtrl', AllProjectsCtrl);

  AllProjectsCtrl.$inject = ['$scope', '$stateParams', '$state', 'Projects', 'commonSrv', 'toastr'];

  function AllProjectsCtrl($scope, $stateParams, $state, Projects, commonSrv, toastr){
    var vm = this;
    vm.statusList = ['backlog', 'progress', 'review', 'rework', 'complete', 'archive']
    vm.projects = Projects.summary(angular.noop, commonSrv.handleError);

  }
})();

