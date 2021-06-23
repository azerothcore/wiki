---
tableofcontents: 1
---

# How to document your code

The extensive Doxygen manual ( https://www.doxygen.nl/manual/docblocks.html ) is well worth browsing. Doxygen provides a wide variety of options for documenting code and can be adapted for general documentation as well. This page well take you through some of the commonly used features in AzerothCore documentation.


Doxygen comment blocks are easy to create. For line comment just insert a triple forward slash.

`///This line will be included in the Doxygen comments for this function/class/file`

Commenting multiple lines is just as easy.

```
/**
These next few lines will form a comment block
To start a new paragraph add an empty line
To end the comment block type asterik and then forward slash.
*/
```

By taking a few minutes as you are writing your code to write comment blocks you can tell future developers what you intended and make their life more productive and easier.

This is an example of a documented [Hook](hooks-script.md) in our `ScriptMgr.h`:

```cpp
/**
 * @brief This hook runs before sending the exit message during the arena queue, allowing you to run extra operations or disabling the exit message
 *
 * @param queue Contains information about the Arena queue
 * @param ginfo Contains information about the group of the queue
 * @return True if you want to continue sending the message, false if you want to disable the message
 */
[[nodiscard]] virtual bool OnBeforeSendExitMessageArenaQueue(BattlegroundQueue* /*queue*/, GroupQueueInfo* /*ginfo*/) { return true; }
```

## Common Doxygen Tags
======================================================================================================================================

### Common Source Document Tags
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`@brief`

This tag supplies a brief description of a function for doxygen pages. This message should tell what happens in the function. By convention in AzerothCore all functions must have brief tags. These included in the header file along with the declaration of the functions.

`@details`

This tag supplies a more detailed description. This message should give a user an idea of when it is valid to call this function( i.e. what must be true for the function to work), how the function carries out it function, and what will be true when the function returns. By convention in AzerothCore all functions must have details tags. These are placed with the definition of the function.

`@param`

This tag can be used to document the purpose and meaning of params for functions. You can specify the nature of the param as input output or both in the following manner

`@param[in]`

`@param[out]`

`@param[in/out]`

`@class`

This tag informs doxygen that the comment block should be associated with the class. This block should explain the purpose of the class, the design considerations, and relation to other classes. Also provide any information other programmers may find useful for using the classes.

`@example`

This tag allows you to insert code snippets which are then collected on the examples page. This way you can tell people how to use your code directly in the file with your class definition.

`@return`

This tag allows you to describe what the function is returning.

### Common Doxygen Page Tags
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

`@page`

This tag tells Doxygen that this is a free floating page and allows doxygen to name the page so that otehr pages can reference and link to the page.

`@page describing_awesome_mode_by_james This Page describes James' Awesome Mode`

The first word after `@page` is the word that will need to be type in a `@ref` command to link the page. Doxygen will replace any references to the page with the string that appears after the word. So in the above case Doxygen would replace "describing_awesome_mode_by_james" with "This Page describes James' Awesome Mode" in the generated documentation. Generally in html as least links are shown in blue. Note that I have had trouble including upper case letters in the "word" naming the page. Sometimes it works as described above, but other times it fails to replace "word" with the "string" for links from other locations.

`@ref`

This command tells Doxgyen to insert a link to the specified page in this section. So following on from the `@page` command above if I wanted to insert a link to the page describing James' awesome mode I would type

`///// @ref describing_awesome_mode_by_james`

`@image`

A picture is sometimes worth a thousand words or so the addage goes at least. This tag allows one to insert an image into the documentation. Doxygen requires different image formats for the different output types. Below I show how to insert images such that they appear in both html and pdfs generated by latex. Note that the image files must be placed in a location recognized by Doxygen. This is set by the IMAGE_PATH variable in the Doxygen file. Currently the doc/images is indexed. So placing the image files in that location should allow Doxygen to find them.

`///// @image html special_image.png`

`///// @image latex special_image.eps "Special Image label" width=5cm`

`@section`

`@subsection`

It is often useful to divide a doxygen page into sections and subsections. The serves two purposes. One it creates headers. Second reference can be created to thorugh the page to link to the section. This page makes of sections and links to sections. The list of section at the beginning of the page is implemented using the `@section` command. Similar to the `@page` command, a link name and string can be provided.

`///// @section common_doxygen_tags_used Common Doxygen Tags`

`///// @subsection common_page_tags Common Doxygen Page Tags`

## Building Documentation
============================================================================================================================================

If doxygen is in your path simply issue the command

`doxygen`
