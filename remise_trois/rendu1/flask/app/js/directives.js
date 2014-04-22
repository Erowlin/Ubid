'use strict';

/* Directives */

var ubidDirectives = angular.module('ubid.directives', []);
ubidDirectives.directive('productItem', function() {
	return {
		restrict: 'A',
		templateUrl: './partials/product-tpl.html'
	};
});