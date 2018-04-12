module.exports = function(grunt) {

  grunt.initConfig({
    concat_css: {
      target : {
        files: {
          'cpag/static/css/app.css': ['bower_components/foundation-sites/dist/css/foundation.css',
          'bower_components/aos/dist/aos.css',
          'cpag/static/css/cpag.css']
        }
      }
    },
    cssmin: {
      target: {
        files: {
          'cpag/static/css/app.min.css': 'cpag/static/css/app.css'
        }
      }
    },
  });

  grunt.loadNpmTasks('grunt-concat-css');
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  grunt.registerTask('default', ['concat_css','cssmin']);

};