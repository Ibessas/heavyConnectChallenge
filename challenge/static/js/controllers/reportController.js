angular.module("reports").controller("reportController",function($scope, userService, reportsService,$http, config){
    $scope.userId= null

    $scope.reload = function(){
        reportsService.getReports($scope.userId ,$scope.offset, $scope.limit).then(function(res){
            $scope.reports = res.data
        });
        userService.getUsers().then(function(res){
            $scope.users = res.data
        })
    }

    $scope.clear = function(){
        $scope.offset = null;
        $scope.limit = null;
        $scope.userId = null;
        $scope.user = null;
        $scope.check = false
        $scope.reload()        
    }

    $scope.check = function(){
        if($scope.limit == 0)
            $scope.limit = null
        
        if($scope.offset == 0)
            $scope.offset = null
    }

    $scope.open = function(item) {
        $scope.selected = item
    };
    
    $scope.$watch('user', function() {
        if ($scope.user == null){
            $scope.userId = null
            $scope.reload()
        }
        $scope.userId = $scope.user.id
        $scope.reload()
    });

});