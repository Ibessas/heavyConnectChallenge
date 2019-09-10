angular.module("reports").controller("reportController",function($scope, $http, reportsAPI, config){
    $scope.userId = {}
    var getReports = function (id, offset,limit) {
        var temp = config.reportUrl 
        if(id != null|| offset != null || limit != null){
            temp += "?"
            if(id!= null)
            temp+="id=" + id +"&"
            if(offset!=null)
            temp+="offset=" + offset + "&"
            if(limit!=null)
            temp+="limit=" + limit
        }

        $http.get(temp).then(function(res){
        $scope.reports = res.data
    });
    }

    var getUsers = function () {
        return $http.get(config.userUrl);
    }

    getReports($scope.user,$scope.offset,$scope.limit);

    $scope.reload = function(){
        getReports($scope.userId ,$scope.offset, $scope.limit);
    }

    $scope.setUser = function(user){
        $scope.userId = user
    }

    getUsers().then(function(res){
        $scope.users = res.data
    });

    $scope.clear = function(){
        $scope.offset = null;
        $scope.limit = null;
        $scope.user = null;
        $scope.check = false
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

    $scope.idSelectedVote = null;
    $scope.setSelected = function (idSelectedVote) {
       $scope.idSelectedVote = idSelectedVote;
    };
    
    $scope.select = function(user) {
        $scope.user = user.id
    };


});