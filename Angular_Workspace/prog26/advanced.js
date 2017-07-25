// Initialization of Angualr app
var testApp = angular.module('testApp', []);

// Head of department
// a controller named mainController in the testApp is created
// $scope is object contains the variables used for binding in the mainController
testApp.controller('mainController', function($scope) {
	$scope.engineers = ["Rajat", "Jitesh", "Varun", "Ankur"];

	$scope.addEngineer = function(name) {
		$scope.engineers.push(name);
	}

	$scope.deleteEngineer = function(name) {
		var index = $scope.engineers.indexOf(name);
		$scope.engineers.splice(index, 1);
	}

});