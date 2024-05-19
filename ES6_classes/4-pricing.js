/* eslint-disable */
export default class Pricing {
	constructor(amount, currency){
	  this._amount = amount;
	  this._currency = currency;
	}
	
	displayFullPrice(){
		return (`${this.amount} ${this.currency.name} (${this.currency.code})`);
	}

	static convertPrice(amount, conversionRate) {
		return amount * conversionRate;
	}

	set amount(newAmount) {
    		this._amount = newAmount;
  	}

  	set currency(currency) {
    		this._currency = currency;
  	}

  	get amount() {
    		return this._amount;
  	}

 	get currency() {
	  	return this._currency;
	}
}
