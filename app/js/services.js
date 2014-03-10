'use strict';

/* Services */

var ubidServices = angular.module('ubid.services', []);
ubidServices.factory('UserService', [function () {
	var usr = {
		isLogged: false,
		username: '',
		firstname: '',
		lastname: '',
		email: '',
		address1: '',
		address2: '',
		city: '',
		country: '',
		postalcode: '',
		userId: ''
	};
	return usr;
}]);