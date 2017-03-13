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
          },
        }
      }
    }
  });

  grunt.registerTask('default', [
  ]);
};
