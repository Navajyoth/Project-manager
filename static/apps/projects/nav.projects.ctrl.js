(function(){
  angular.module('app')
  .controller('NavProjectsCtrl', NavProjectsCtrl);

  NavProjectsCtrl.$inject = ['$scope', '$stateParams', '$state', 'Projects', 'commonSrv', 'toastr'];

  function NavProjectsCtrl($scope, $stateParams, $state, Projects, commonSrv, toastr){
    var vm = this;

    Projects.query(function(projects){
      vm.projects = projects;
      // vm.project = _.findWhere(projects, {id:Number($stateParams.projectId)});
    });

    vm.move = function(delta){
      var index = _.indexOf(projects, vm.project) + delta;
      if(projects.length > index && index > -1){
        $state.go('project', {projectId:projects[index].id})
      }
    }
  }
})();


