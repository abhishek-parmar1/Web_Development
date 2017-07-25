// Initialization of Angualr app
var testApp = angular.module('testApp', ['ngRoute']);



testApp.config(function ($routeProvider){
        $routeProvider.when('/', {
            templateUrl : 'pages/loginTemplate.html',
        });
        $routeProvider.when('/home', {
            templateUrl : 'pages/homeTemplate.html',
        });
});

testApp.controller('mainController', function($scope) {
    console.log("hell");
});

testApp.controller('loginController', function($scope) {
    console.log("login");
});