(function(){
  angular.module('app')
    .factory('Tasks', Tasks);

  Tasks.$inject = ['$http', '$resource', 'commonSrv'];

  function Tasks($http, $resource, commonSrv){
    var URL = '/api/tasks/'
      var Task = $resource(URL + ':id/:sub/?userid=:userId', {
        id:'@id',
      },{
        update: {method:'PUT'},
        user: {method:'GET', params:{sub:'user', userid: '@userId'}, isArray:true},
        notify: {method:'GET', params:{id:'@id', sub:'notify'}},
      });
    return Task;
  }
})();

