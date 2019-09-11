angular.module("reports").factory("userService", function($http, config){
    var _getUsers = function () {
        return $http.get(config.userUrl);
    }
    
    return{
        getUsers: _getUsers
    }
})