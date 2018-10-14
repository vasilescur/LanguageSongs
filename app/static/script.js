// Initialize selector drop-downs
$(document).ready(function () {
    $('select').formSelect();


    // plz no hack
    const apiKey = "AIzaSyChPUazt0gK4qMjVJDpo8hPE49QAUfZW4w";

    // Set endpoints
    const endpoints = {
        translate: "",
        detect: "detect",
        languages: "languages"
    };

    // Abstract API request function
    function makeApiRequest(endpoint, data, type) {
        url = "https://www.googleapis.com/language/translate/v2/" + endpoint;
        url += "?key=" + apiKey;

        // If not listing languages, send text to translate
        if (endpoint !== endpoints.languages) {
            url += "&q=" + encodeURI(data.text);
        }

        // If translating, send target and source languages
        if (endpoint === endpoints.translate) {
            url += "&target=" + data.target;
            url += "&source=" + data.source;
        }

        // Return response from API
        return $.ajax({
            url: url,
            type: type || "GET",
            data: data ? JSON.stringify(data) : "",
            dataType: "json",
            async: false,
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json"
            }
        });
    }

    function translate(text, source, target) {
        res = makeApiRequest(endpoints.translate, {
            'text': text,
            'source': source,
            'target': target
        }, 'GET');

        return res;
    }

    // Convert country code to country name
    function getLanguageNames() {
        return $.getJSON("https://api.myjson.com/bins/155kj1");
    }


    const INITIAL_CONTENT = 'Loading...'

    const state = {
        isFetching: false,
        canFetch: true
    }

    $('.translatable').each(function (i, obj) {
        console.log('Tipping ' + obj);

        var that = $(this);

        tippy('#a' + i, {
            content: INITIAL_CONTENT,
            arrow: true,

            async onShow(tip) {
                if (state.isFetching || !state.canFetch) return

                state.isFetching = true
                state.canFetch = false

                try {

                    console.log('Fetching');
                    console.log(that);

                    const original = that.text();

                    const response = translate(original, 'de', 'en');
                    const text = response.responseJSON.data.translations[0].translatedText;

                    console.log(original + ' --> ' + text);

                    if (tip.state.isVisible || true) {
                        tip.setContent(text);
                    }
                } catch (e) {
                    tip.setContent(`Fetch failed. ${e}`)
                } finally {
                    state.isFetching = false
                }
            },
            onHidden(tip) {
                state.canFetch = true
                tip.setContent(INITIAL_CONTENT)
            }
        });
    });




    // $('.translatable').hover(function () {
    //     if ($(this).attr('translated_yet') == 'false') {
    //         $(this).attr('translated_yet', 'true');

            

    //         $(this).attr('data-tippy', text);

    //         console.log('Changed to ' + text);
    //         console.log($(this));
    //     }

        // console.log($(this).attr('translated_yet'));
        // tippy.update();
    });
// });