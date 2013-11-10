angular.module('thumper', ['ui.bootstrap']);

var tabs = [
    { 'title':"Tab 1", 'content':'Text Body 1' },
    { 'title':"Tab 2", 'content':'Text Body 2' },
    { 'title':"Tab 3", 'content':'Text Body 3' }
]

function TabbedViewCtrl($scope) {
    $scope.tabs = tabs
}


function food_selector($scope) {

    $scope.selection = [ 'None' ]

    $scope.set_choices =  function(options) {
        $scope.options = options;
    }
        
    $scope.select_item = function(name) { 
        $scope.selection.push(name);
    }

    $scope.appetizers = '0'
}
