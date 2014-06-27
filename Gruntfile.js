//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
var fs = require('fs');
var path = require('path');
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
var websiteRoot = "website/build/";
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module.exports = function(grunt) {
  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - ' +
                '<%= grunt.template.today("yyyy-mm-dd") %> */',
        compress: {
            drop_console: true
        }
      },
      website: {
        files: [
            {
                expand: true,
                cwd:  websiteRoot,
                ext: '.js',
                src: [
                    '**/*.js',
                    '!**/*min.js',
                ],
                dest: websiteRoot
            }
        ],
      }
    },
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    prettify: {
      website: {
        options: {
            config: '.prettifyrc'
        },
        files: [
            {
                expand: true,
                cwd:  websiteRoot,
                ext: '.html',
                src: ['**/*.html'],
                dest: websiteRoot
            }
        ],
      }
    },
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    'gh-pages': {
        website: {
          options: {
            base: 'website/build/',
            branch: 'master'
          },
          src: ['**']
        }
    }
  });
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // Load tasks.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-gh-pages');
  grunt.loadNpmTasks('grunt-prettify');
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // Default task: move everything to the 'build' folder.
  grunt.registerTask('default', ['uglify', 'prettify', 'gh-pages']);
};
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
