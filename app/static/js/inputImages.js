function handleFileSelect(evt) {
    var files = evt.target.files;

    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {

        // Only process image files.
        if (!f.type.match('image.*')) {
            continue;
        }

        var reader = new FileReader();

        // Closure to capture the file information.
        reader.onload = (function (theFile) {
            return function (e) {
                // Render thumbnail.
                var span = document.createElement('span');
                span.innerHTML =
                        [

                            '<input id="', escape(theFile.name),'" class="radioImage" type="radio" name="image" value="', escape(theFile.name), '"/>',
                            '<label class="imageSelector" for="', escape(theFile.name),'">',
                            '<img class="image" style="height: 75px; border: 1px solid #000; margin: 5px" src="',
                            e.target.result,
                            '" title="', escape(theFile.name),
                            '"/></label>'

                        ].join('');

                document.getElementById('imageList').insertBefore(span, null);
            };
        })(f);

        // Read in the image file as a data URL.
        reader.readAsDataURL(f);
    }
}

document.getElementById('inputImages').addEventListener('change', handleFileSelect, false);
