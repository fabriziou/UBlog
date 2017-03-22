module.exports = function(grunt) {
  require('load-grunt-tasks')(grunt);

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    bower: {
      install: {
        options: {
          targetDir: 'src/static/',
          cleanTargetDir: false,
          layout: function(type, component, source) {
              return type;
          }
        }
      }
    },
    sass: {
      dist: {
        files: {
          'src/static/css/master.css': ['src/static/sass/master.scss']
        }
      }
    }
  });

  grunt.registerTask('default', [
  ]);
};
