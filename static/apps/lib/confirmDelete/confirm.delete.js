  (function(){angular.module('app').directive('confirmDelete', function(){
    return {
      restrict: 'E',
      templateUrl: '/static/apps/lib/confirmDelete/confirm.delete.html',
      scope: {
        onConfirm:'&',
      },
      link: function(scope, element, attrs){

      },
    }
  });

})();