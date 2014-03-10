'use strict';

/* Services */

var ubidServices = angular.module('ubid.services', []);
ubidServices.factory('UserService', [function () {
	var usr = {
		isLogged: false,
		username: '',
		userId: ''
	};
	return usr;
}]);