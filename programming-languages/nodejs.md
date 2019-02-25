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
