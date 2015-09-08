(function(){
  angular.module('app')
  .directive('task', function(Tasks, Commits, Users, commonSrv, $state, $stateParams, toastr){
    return {
      restrict: 'E',
      templateUrl: '/static/apps/tasks/html/task.html',
      scope: {
        task:'=',
        index:'=',
        showEdit:'@',
        showProject:'@',
        showUser:'@',
        showStatus:'@',
        showNotify:'=',
      },
      link: function(scope, element, attrs){
        var orgTask;
        scope.times = ['estimated_time', 'actual_time', 'rework_time'];
        scope.colors = ['#112233', '#19f', '#e95', '#F1C40F', '#27AE60', '#C0392B', '#F39C12', '#112233', '#112233', '#112233', '#112233', '#112233', ]
        scope.taskHrcy = {
          backlog: {
            next: 'progress',
            // timeField: 'estimated_time',
            // timeText: 'Self Estimate'
          },
          rework:{
            next: 'review',
            timeField: 'rework_time',
            timeText: 'Rework Time'
          },
          progress:{
            next: 'review',
            prev: 'backlog',
            timeField: 'actual_time',
            timeText: 'Time Taken'
          },
          review:{
            next: 'complete',
            prev: 'rework',
          },
          complete:{
            prev:'rework',
            next:'archive',
          }
        }

        init();
        function init(){
          scope.times.forEach(function(t){
            scope.task[t] = parseInt(scope.task[t]);
          })
          scope.editTs =  !Boolean(scope.task.id);
          updateOrg();
          Users.queryCached().then(function(users){
            scope.users = users;
            scope.taskUser = _.findWhere(users, {id:scope.task.user});
            console.log(scope.task.user);
          });
          scope.priorityOpts = ['low', 'normal', 'high', 'urgent']
        }

        scope.move = function(dir){
          var statusInfo = scope.taskHrcy[scope.task.status];
          scope.task.status = statusInfo[dir];
          scope.upsert();
        }

        scope.$watch('taskUser', function(value){
          if(value && (value.id != scope.task.user)){
            scope.task.user = value.id;
          } 
        });

        scope.delete = function(){
          var status = confirm('Are you sure you want to delete task ' + scope.task.title + ' ?');
          if(status){
            scope.task.status = 'cancelled';
            scope.upsert('Deleting Task...', onDelete)
          }
          function onDelete(){
            toastr.success('Deleted Task');
          }
        }

        scope.upsert = function(msg, callback){
          toastr.info(msg || 'Updating Task...');
          var task = new Tasks(scope.task);
          callback = callback || onSave;
          if(scope.task.id){
            task.$update(callback, commonSrv.handleError);
          } else {
            task.$save(callback, commonSrv.handleError);
          }
          clearEdit();
        }

        scope.notify = function(){
          var task = new Tasks(scope.task);
          task.$notify(function(){
            toastr.info('Notification send for ' + scope.task.title);
          }, commonSrv.handleError);
        }

        scope.addCommit = function(){
          var url = prompt('Enter commit url?');
          if(url){
            var commit = new Commits({
              url:url,
              task:scope.task.id,
            })
            commit.$save(function(com){
              scope.task.commits = (scope.task.commits || []);
              scope.task.commits.push(com);
            }, commonSrv.handleError);
          }
        }

        scope.deletecommit = function(c){
          var sure = confirm("Are you sure want to delete this commit?");
          if (sure){
            var commit = new Commits({id: c.id});
            commit.$delete(function(){
              c.deleted = true;
            });
          } 
        } 

        scope.cancel = function(){
          if(scope.task.id){
            scope.task = angular.copy(orgTask);
            clearEdit();
          } else {
            scope.task.status = 'cancelled';
            // scope.$emit(events.task.deleted);
          }
        }

        function onSave(task){
          toastr.success("Updated Task");
          _.extend(scope.task, task);
          updateOrg();
        }

        function clearEdit(){
          scope.edit = false;
        }

        function updateOrg(){
          orgTask = angular.copy(scope.task);
        }
      },
    }
  })

  .directive('lockedTask', function(Tasks, commonSrv, events, $state, $stateParams, toastr, Upload){
    return {
      restrict: 'E',
      templateUrl: '/static/apps/tasks/html/locked.task.html',
      scope: {
        task:'=',
        index:'=',
      },
      link: function(scope, element, attrs){
      },
    }
  })

})();

