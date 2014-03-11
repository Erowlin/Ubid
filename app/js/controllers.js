'use strict';

/* Controllers */

var ubidControllers = angular.module('ubid.controllers', []);

ubidControllers.controller('HeaderCtrl', ['$scope', '$rootScope', '$http', '$location', 'UserService',
	function($scope, $rootScope, $http, $location, User) {
		$rootScope.headerTemplate = User.isLogged ? 'partials/header.html' : 'partials/header-login.html';
		$scope.logout = function() {
			$http({method:'POST', url:'http://localhost:5000/user/logout', data: {"token" : User.token, "user_id": User.id}}).
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
				User.token = data.token;
				User.id = data.user_id;
				User.isLogged = true;
				$rootScope.headerTemplate = 'partials/header.html';
				$location.path("/");
			}).
			error(function(status, response){
				$scope.err = true;
				$scope.errorMsg = "Erreur d'authentification: Mauvais mot de passe et/ou username."
			});
		};
	}]);

ubidControllers.controller('RegisterCtrl', ['$scope', '$http', 'UserService',
	function($scope, $http, User) {
		$scope.EMAIL_REGEXP = /^[a-z0-9!#$%&'*+/=?^_`{|}~.-]+@[a-z0-9-]+(\.[a-z0-9-]+)*$/i;
		$scope.register = function() {
			$scope.user.token = User.token;
			$scope.user.id = User.id;
			$http({method:'POST', url:'http://localhost:5000/user/', data: $scope.user})
			.success(function(status, response){
				$location.path("/");
				console.log("Inscription réussie!");
			})
			.error(function(status, response){
				console.log(status);
			});
		};
	}]);

ubidControllers.controller('AccountBarCtrl', ['$scope',
	function($scope) {
	}]);

ubidControllers.controller('UserAccountCtrl', ['$scope', '$http','UserService',
	function($scope, $http, User) {
		$scope.editMode = false;

		$http.get('http://localhost:5000/user/' + User.id + '?token=' + User.token + '&user_id=' + User.id).
		success(function(data, status){
			User = data.user;
			$scope.info = data.user;
		}).
		error(function(data, status){
			console.log(status + ": " + data);
		});

		$scope.saveChanges = function() {
			console.log($scope.info);
			console.log(User);
			$scope.info.token = User.token;
			$scope.info.user_id = User.id;
			console.log($scope.info);
			$http.post('http://localhost:5000/user/' + User.id, $scope.info).
			success(function(data, status){
				User = $scope.info;
				$scope.editMode = false;
			}).
			error(function(data, status){
				console.log(data);
			});
		};
	}]);

ubidControllers.controller('UserProfileCtrl', ['$scope', '$routeParams',
	function($scope, $routeParams) {
		$scope.userId = $routeParams.userId;
		$scope.test = { user: { username: "Kiki", city: "Le Mans",  firstname: "Jean-Michel"} };
		$scope.user = $scope.test.user;
	}]);

ubidControllers.controller('ProductPageCtrl', ['$scope', '$routeParams', 'UserService', 
	function($scope, $routeParams){
		$scope.productId = $routeParams.productId;
		$http.get('http://localhost:5000/product/' + $scope.productId + '?token=' + User.token + '&user_id=' + User.id).
		success(function(data, status){
			$scope.product = data.product;
		}).
		error(function(data, status){
			console.log(status + ": " + data);
		});
	}]);

ubidControllers.controller('ProductListCtrl', ['$scope',
	function($scope){
		// $scope.products = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8']; // GET /products/
		$scope.products = { product:  {value: 2,label: "Dubstep",value2: 3,label1: "BoysIIMen",value3: 4,label3:"Sylenth1"} };

		var tmp = [];
		var keys = Object.keys($scope.products.product);
		keys.forEach(function(key){
			tmp.push($scope.products.product[key]);
		});

		$scope.maxCols = 4;
		$scope.rows = tmp.chunk($scope.maxCols);
	}]);

ubidControllers.controller('SalesCtrl', ['$scope',
	function($scope) {
		$scope.products = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8'];
	}]);