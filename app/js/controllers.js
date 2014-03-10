'use strict';

/* Controllers */

var ubidControllers = angular.module('ubid.controllers', []);

ubidControllers.controller('HeaderCtrl', ['$scope', '$rootScope', '$http', '$location', 'UserService',
	function($scope, $rootScope, $http, $location, User) {
		$rootScope.headerTemplate = User.isLogged ? 'partials/header.html' : 'partials/header-login.html';
		$scope.logout = function() {
			$http({method:'POST', url:'http://localhost:5000/user/logout'}).
			success(function(e){
				User.isLogged = false;
				$rootScope.headerTemplate = 'partials/header-login.html';
				$location.path("/");
			}).
			error(function(status, response){
				console.log("logout: Une erreur est survenue : [" + status + "] " + response);
			});
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
		$scope.login = function() {
			$http({method:'POST', url:'http://localhost:5000/user/login', data: {"username" : $scope.uname, "password": $scope.passwd}}).
			success(function(data){
				User.userId = data.userId;
				User.isLogged = true;
				$rootScope.headerTemplate = 'partials/header.html';
				$location.path("/");
			}).
			error(function(status, response){
				console.log("Raté!");
			});
		};
	}]);

ubidControllers.controller('RegisterCtrl', ['$scope', '$http', 'UserService',
	function($scope, $http, User) {
		$scope.register = function() {
			var data = $scope.user;
			$http({ method:'POST',
				url:'http://localhost:5000/user',
				data: {
					"username" : $scope.user.username,
					"firstname" : $scope.user.firstname,
					"lastname" : $scope.user.lastname,
					"address1" : $scope.user.address1,
					"address2" : $scope.user.address2,
					"city" : $scope.user.city,
					"postalcode" : $scope.user.postalcode,
					"country" : $scope.user.country,
					"email" : $scope.user.email,
					"password" : $scope.user.password
				}
			}).
			success(function(status, response){
				console.log("Inscription réussie!");
			}).
			error(function(status, response){
				console.log("L'inscription a échoué!");
			});
		};
	}]);

ubidControllers.controller('AccountBarCtrl', ['$scope',
	function($scope) {
	}]);

ubidControllers.controller('UserAccountCtrl', ['$scope', '$http','UserService',
	function($scope, $http, User) {
		$scope.editMode = false;
		// $scope.saveChanges = function() {
		// 	// envoyer donnees
		// 	console.log("Données sauvegardées !");
		// 	$scope.editMode = false;
		// }

		$http.get('http://localhost:5000/user/' + User.userId).
		success(function(data, status){
			User.username = data.user.username;
			$scope.username = User.username;
		}).
		error(function(data, status){
			console.log(status + ": " + data);
		});
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