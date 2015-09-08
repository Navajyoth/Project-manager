(function(){
  angular.module('app')
  .factory('Projects', Projects);

  Projects.$inject = ['$http', '$resource', 'commonSrv'];

  function Projects($http, $resource, commonSrv){
    var URL = '/api/projects/'
    var Project = $resource(URL + ':id/:sub/', {
      id:'@id',
    },{
        tasks: {method:'GET', params:{id:'@id', sub:'tasks'}, isArray:true},
        summary: {method:'GET', params:{ sub:'summary'}, isArray:true},
    });
    return Project;
  }
})();
