'use strict';

/* Controllers */

var ubidControllers = angular.module('ubid.controllers', []);
ubidControllers.controller('HeaderCtrl', ['$scope', '$rootScope', 'UserService',
	function($scope, $rootScope, User) {
		$rootScope.headerTemplate = User.isLogged ? 'partials/header.html' : 'partials/header-login.html';
		$scope.logout = function() {
			User.isLogged = false;
			$rootScope.headerTemplate = 'partials/header-login.html';
		};
	}]);

ubidControllers.controller('SearchCtrl', ['$scope',
	function($scope) {
	}]);

ubidControllers.controller('SearchResultCtrl', ['$scope',
	function($scope) {
		$scope.result = ['item1', 'item2', 'item3', 'item4', 'item5']; // search
		$scope.maxCols = 4;
		$scope.rows = $scope.result.chunk($scope.maxCols);
	}]);

ubidControllers.controller('LandingCtrl', ['$scope',
	function($scope) {

	}]);

ubidControllers.controller('LoginCtrl', ['$scope', '$rootScope', '$location', '$http', 'UserService',
	function($scope, $rootScope, $location, $http, User) {
		$scope.login = function() { //tmp
			// User.username = username;
			// User.isLogged = true;
			// $rootScope.headerTemplate = 'partials/header.html';
			// $location.path("/");
			var data = $scope.info;
			console.log(data);
			// $http({method:'POST', url:'http://localhost:5000/user/login'}, data).
			// success(function(data, status){
			// 	console.log(status + ": " + data);
			// }).
			// error(function(data, status){
			// 	console.log(status + ": " + data);
			// });
			$http({method:'GET', url:'http://localhost:5000/user/1'}).
			success(function(data, status){
				console.log(status + ": " + data);
			}).
			error(function(data, status){
				console.log(status + ": " + data);
			});
		};
	}]);

ubidControllers.controller('RegisterCtrl', ['$scope', '$http', 'UserService',
	function($scope, $http, User) {
		// $scope.register = function() {
		// 	var data = $scope.user;
		// 	$http({method:'POST', url:'http://localhost:5000/user/'},data).
		// 	success(function(status, response){
		// 		console.log("Recu!");
		// 	}).
		// 	error(function(status, response){
		// 		console.log("Raté!");
		// 	});
		// };
	}]);

ubidControllers.controller('AccountBarCtrl', ['$scope',
	function($scope) {
	}]);

ubidControllers.controller('UserAccountCtrl', ['$scope', 'UserService',
	function($scope, User) {
		$scope.editMode = false;
		$scope.saveChanges = function() {
			// envoyer donnees
			console.log("Données sauvegardées !");
			$scope.editMode = false;
		}
	}]);

ubidControllers.controller('UserProfileCtrl', ['$scope', '$routeParams',
	function($scope, $routeParams) {
		$scope.userId = $routeParams.userId;
	}]);

ubidControllers.controller('ProductPageCtrl', ['$scope', '$routeParams',
	function($scope, $routeParams){
		$scope.productId = $routeParams.productId;
	}]);

ubidControllers.controller('ProductListCtrl', ['$scope',
	function($scope){
		$scope.products = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8']; // GET /products/
		$scope.maxCols = 4;
		$scope.rows = $scope.products.chunk($scope.maxCols);
	}]);

ubidControllers.controller('SalesCtrl', ['$scope',
	function($scope) {
		$scope.products = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8'];
	}]);