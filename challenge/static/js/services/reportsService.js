angular.module("reports").factory("reportsAPI", function($http, config){
    var _getReports = function (id, offset,limit) {
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

    return{
        getReports: _getReports
    }
})