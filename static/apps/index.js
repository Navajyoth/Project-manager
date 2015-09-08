(function(){
  Angular.createApp('app', ['ngDragDrop', 'cgBusy','dndLists','ui.bootstrap']);

  angular.module('app')
  .directive('pageTitle', ['$rootScope', '$timeout',
    function($rootScope, $timeout) {
      return {
        link: function(scope, element) {
          var listener = function(event, toState) {
            if (toState.data && toState.data.title) title = toState.data.title + " | ProMan";
            $timeout(function() {
              element.text(title);
            }, 0, false);
          };
          $rootScope.$on('$stateChangeSuccess', listener);
        }
      };
    }
  ])


})();
