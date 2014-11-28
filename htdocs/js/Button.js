var TButton = function (x, y, width, height, text, colour) {
        this.x = x || 0;
        this.y = y || 0;
	this.width = width || 0;
	this.height = height || 0;
	this.text = text;
	this.colour = colour || "cyan";
};

TButton.prototype = {
        getX: function () {
		return this.x;
	},

	getY: function () {
		return this.y;
	},

	getWidth: function () {
		return this.width;
	},

	getHeight: function () {
		return this.height;
	},

	getText: function () {
		return this.text;
	},

	getColour: function () {
		return this.colour;
	}

};
*/
