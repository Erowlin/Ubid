'use strict';

/* Services */

var ubidServices = angular.module('ubid.services', []);
ubidServices.factory('UserService', [function () {
	var usr = {
		token: '',
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
		user_id: ''
	};
	return usr;
}]);