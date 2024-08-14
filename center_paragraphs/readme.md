# Center a paragraph

## input

paragraph is an array of word arrays like
`[['hello', 'world'], ['This','text','isjustified','now'], ['lets','see','this']]`

width is an integer of the max width to account for `width = 16`

words cannot be seperated, must be held together on same line

there will be `*` surrounding the text

example output

```python
  paragraph = [
    '******************',
    '*  hello world   *',
    '*   This text    *',
    '*  isjustified   *',
    '*  now lets see  *'
    '*      this      *',
    '******************'
  ]
```
