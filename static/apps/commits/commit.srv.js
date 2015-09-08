(function(){
  angular.module('app')
    .factory('Commits', Commits);

  Commits.$inject = ['$http', '$resource', 'commonSrv'];

  function Commits($http, $resource, commonSrv){
    var URL = '/api/commits/'
      var Commit = $resource(URL + ':id/:sub/', {
        id:'@id',
      },{
        update: {method:'PUT'},
        user: {method:'GET', params:{sub:'user'}, isArray:true},
        // tasks: {method:'GET', params:{id:'@id', sub:'tasks'}, isArray:true},
      });
    return Commit;
  }
})();


