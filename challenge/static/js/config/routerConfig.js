angular.module("reports").config(function($routeProvider){
    $routeProvider.when("", {
        templateUrl:"views/reportsData.html",
        controller:"reportController",
        resolve: {
            reports: function(reportsAPI) {
                return reportsAPI.getReports();
            }
        }
    })
})