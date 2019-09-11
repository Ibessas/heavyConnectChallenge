angular.module("reports").factory("reportsService", function($http, config){
    var _getReports = function (id, offset,limit) {
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
        return $http.get(temp)
    }

    return{
        getReports: _getReports
    }
})