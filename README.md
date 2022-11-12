# highlighted-tana-paste
Tana Paste code for highlighted app

I use [Highlighted](https://highlighted.app/) to highlight snippets of text while reading physical books. To export these highlights into [Tana](https://tana.inc/), I have created `highlighted.py` file. It creates a string that is interpreted by Tana to store data.

Code creates two supertags:
1. `#book`
2. `#highlighted`

Very first node created is `#book`, which has fields `Author` and `ISBN`.<br>
After that all other nodes are of `#highlight` type which has fields:
1. `Book`(which book this highlight belong to)
2. `Page`
3. `Tags`
4. `Notes`<br>

I am not able to `@` link `Book` field in `#highlight` supertag with `#book` node. If someone knows how to do it, let me know.

Screenshot of first time pasting highlights into Tana.
<img width="952" alt="Screenshot 2022-11-12 at 12 51 49 AM" src="https://user-images.githubusercontent.com/8711912/201459543-25c16a13-fec3-4fea-8e65-0be2bb1ce5d0.png">
