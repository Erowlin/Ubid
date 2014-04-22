'use strict';

/* App Module */

var ubidApp = angular.module('ubidApp', [
  'ngRoute',
  'ngCookies',
  'ubid.controllers',
  'ubid.directives',
  'ubid.services'
  ]);

ubidApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
  when('/', {
    templateUrl: './partials/landing.html',
    controller: 'LandingCtrl',
    publicAccess: true
  }).
  when('/login', {
    templateUrl: 'partials/login.html',
    controller: 'LoginCtrl',
    publicAccess: true
  }).
  when('/register', {
    templateUrl: 'partials/register.html',
    controller: 'RegisterCtrl',
    publicAccess: true
  }).
  when('/profile', {
    templateUrl: './partials/account.html',
    controller: 'UserAccountCtrl'
  }).
  when('/profile/:userId', {
    templateUrl: './partials/profile.html',
    controller: 'UserProfileCtrl',
    publicAccess: true
  }).
  when('/product/:productId', {
    templateUrl: './partials/product.html',
    controller: 'ProductPageCtrl',
    publicAccess: true
  }).
  when('/search', {
    templateUrl: './partials/search-result.html',
    controller: 'SearchResultCtrl',
    publicAccess: true
  }).
  when('/sell', {
    templateUrl: './partials/sell.html',
    controller: 'SalesCtrl'
  }).
  otherwise({
    redirectTo: '/'
  });
}]);

ubidApp.config(['$httpProvider', function($httpProvider) {
  $httpProvider.defaults.useXDomain = true;
  delete $httpProvider.defaults.headers.common['X-Requested-With'];
}]);

ubidApp.run(['$rootScope', '$location', 'UserService', function($rootScope, $location, User) {
  $rootScope.$on('$routeChangeStart', function(event, next, current) {
    var publicAccess = next.publicAccess || false;
    if (!User.isLogged && !publicAccess)
      $location.path('/login').replace();
  });
}]);