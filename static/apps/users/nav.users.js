(function(){
  angular.module('app')
  .controller('NavUsersCtrl', NavUsersCtrl);

  NavUsersCtrl.$inject = ['$scope', '$stateParams', '$state', 'Users', 'commonSrv', 'toastr'];

  function NavUsersCtrl($scope, $stateParams, $state, Users, commonSrv, toastr){
    var vm = this;

    vm.users = Users.query(function(){
      // vm.user = _.findWhere(users, {id:Number($stateParams.userId)});
    });

    // vm.move = function(delta){
    //   var index = _.indexOf(users, vm.user) + delta;
    //   if(users.length > index && index > -1){
    //     $state.go('user', {userId:users[index].id})
    //   }
    // }
  }
})();



