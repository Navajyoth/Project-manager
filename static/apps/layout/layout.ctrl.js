(function(){
  angular.module('app')
    .controller('LayoutCtrl', LayoutCtrl);


  LayoutCtrl.$inject = ['$scope', '$rootScope', 'Users', 'commonSrv', '$q'];

  function LayoutCtrl($scope, $rootScope, Users, commonSrv, $q){
    var vm = this;

    init();
    function init(){
      vm.user = Users.get({id:'self'}, angular.noop, commonSrv.handleError);
      $scope.$on('$stateChangeStart', function(event, toState, toParams, fromState, fromParams) {
        if (toState.resolve) {
          $rootScope.busy = true;
        }
      });
      $scope.$on('$stateChangeSuccess', function(event, toState, toParams, fromState, fromParams) {
        if (toState.resolve) {
          $rootScope.busy = false;
        }
      });

    }
  }

})();
