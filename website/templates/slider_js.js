{% macro js( mediabar ) -%}

// Set up Sliders
// **************
$(function(){

    $("#slider1").anythingSlider({
        resizeContents      : false, // If true, solitary images/objects in the panel will expand to fit the viewport
        navigationFormatter : function(index, panel){
            return [
                {% for data in mediabar %}
                    "{{ data.title }}",
                {% endfor %}
            ][index - 1];
        },
        onSlideComplete : function(slider){
            // alert("Welcome to Slide #" + slider.currentPage);
        }
    });
});
{%- endmacro %}
