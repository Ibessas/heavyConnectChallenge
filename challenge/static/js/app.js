var app = angular.module("reports",[])
app.controller("api",function($scope, reportsAPI){
    reportsAPI.getReports(-1,3,1)
    .then(function(res){
        console.log(res)
    }).catch(function(err) {
      
    });
});

