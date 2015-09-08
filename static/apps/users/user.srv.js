(function(){
  angular.module('app')
  .factory('Users', Users);

  Users.$inject = ['$http', '$resource', 'commonSrv', '$q'];

  function Users($http, $resource, commonSrv, $q){
    var users;
    var deferred = $q.defer();
    var URL = '/api/users/'
    var User = $resource(URL + ':id/:sub/', {
      id:'@id',
    },{
       update: {method:'PUT'},
        // tasks: {method:'GET', params:{id:'@id', sub:'tasks'}, isArray:true},
    });
    User.query(function(result){
      users = result;
      deferred.resolve(users);
    });
    User.queryCached = function(){
      if(users){
        deferred.resolve(users);
      }
      return deferred.promise;
    }
    return User;
  }
})();


