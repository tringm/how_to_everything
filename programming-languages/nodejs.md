## testSuite
### Supertest - Sample

```
describe('Test Find - populating data @populating-normal', () => {
	it('should return 200 OK when trying to populate data', async () => {
	...
	})
})
```
### Mocha -tags

Tags: @populating-normal

```
describe('Test Find - populating data @populating-normal'
```

### Mocha - pass parameter

```
--grep @tag
--grep @tag --invert
```

If in npm: => Add --

```
npm test -- --grep @tag
```


## React

### Multi-options dropdown
1. Use [semantic-ui-react](https://react.semantic-ui.com/usage)
	* Remember to use to install **BOTH** **semantic-ui-react** and **semantic-ui-css**
	* [Dropdown docs](https://react.semantic-ui.com/modules/dropdown/)
	* To trigger event of selection:
		```js
		handleOnChange = (e, data) => {
	        const val = data.value;
	        const key = data.options[0].key;
	        const state = this.state;
	        state.args.values[key] = vals.join(' ');
	        this.setState(state);
	        this.update();
	    };

		<Dropdown
			fluid
			multiple
			search
			selection
			onChange={self.handleOnChange.bind(self)}
			options={options}
		/>
		```
		In the handleOnChange, the val is the value of the selection. The key is get kinda hackish by using the key value in the options. This example is for multiple dropdowns.

1. Delay onchange event (e.g: Finish typing a word):
	```js
	const WAIT_INTERVAL = 500;

	handleOnChange(propertyInputs) {
        if (this._timeout) {
            clearTimeout(this._timeout);
        }
		this._timeout = setTimeout(() => {
			this._timeout = null;
			this.triggerChange();
		}, WAIT_INTERVAL);
    }

	<Input
        onChange={self.handleOnChange.bind(self)}
        type="text"
        name={name}
        id={p}
        placeholder={name}
    />
	```

1. Nice format table
	* Use [react-table](https://www.npmjs.com/package/react-table#data)
		* ***NOTE***: Remember to import css
			```js
			import "react-table/react-table.css";
			```
