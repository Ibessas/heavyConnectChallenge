angular.module("reports").controller("reportController",function($scope, $http, reportsAPI, config){
    var getReports = function (id, offset,limit) {
        if(id != null|| offset != null || limit != null){
            config.baseUrl += "?"
            if(id!= null)
                config.baseUrl+="id=" + id +"&"
            if(offset!=null)
                config.baseUrl+="offset=" + offset + "&"
            if(limit!=null)
                config.baseUrl+="limit=" + limit
        }
        return $http.get(config.baseUrl);
    }
    getReports().then(function(res){
        $scope.reports = res.data
    });

    $scope.open = function(item) {
        $scope.selected = item
    };

    $scope.idSelectedVote = null;
    $scope.setSelected = function (idSelectedVote) {
       $scope.idSelectedVote = idSelectedVote;
    };
});