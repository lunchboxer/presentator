module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: {
      //options: {
        //includePaths: ['components/foundation/scss']
      //},
      debug: {
        options: {
            style: 'expanded',
            debugInfo: true,
            sourceComments: 'map'
        },
        files: {
          'css/app.debug.css': 'scss/app.scss',
          'css/show.debug.css': 'scss/show.scss'
        }        
      },
      min: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          'css/app.css': 'scss/app.scss',
          'css/show.css': 'scss/show.scss'
        }        
      }
    },
    uglify: {
        common: {
            files: {
                'js/combined.min.js': ['js/lib/jquery.min.js',
                                       'js/lib/autobahn.min.js', 
                                       'js/lib/fastclick.js',
                                       'js/lib/foundation.js', 
                                       'js/lib/foundation.alert.js',
                                       'js/lib/foundation.abide.js',
                                       'js/lib/foundation.topbar.js']
            }
        },
        show: {
            files: {
                'js/show_combined.min.js': ['js/lib/jquery.min.js',
                                            'js/lib/underscore-min.js',
                                            'js/lib/bigtext.js',
                                            'js/lib/autobahn.min.js']
            }
        }
    },
    watch: {
      grunt: { files: ['Gruntfile.js'],
                tasks: 'default'},

      sass: {
        files: 'scss/**/*.scss',
        tasks: ['sass']
      },
      js: {
        files: 'js/lib/*.js',
        tasks: ['concat:common', 'uglify']
      },
      staticdirs: {
        files: ['js/*.js', 'css/*.css', 'img/*', 'fonts/*', 'index.html', 'robots.txt'],
        tasks: ['exec:collectstatic']
      }
    },
    exec: {
        collectstatic: {
            cmd: function(){
                var python = '$WORKON_HOME/presentator/bin/python';
                var command = '$PROJECT_HOME/presentator/manage.py collectstatic --noinput';
                var ignore = ['*.scss', 'node_modules', 'Gruntfile.js', 'package.json'];
                return python + ' ' + command + ' --ignore ' + ignore.join(' --ignore ');
            }
        }
    }

  });

  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-exec');

  grunt.registerTask('build', ['sass', 'uglify', 'exec:collectstatic']);
  grunt.registerTask('default', ['build','watch']);
  //grunt.registerTask('collect-static', 'Symlink static files using Django utility', function(){
        //run "./bin/manage.py collectstatic --link --noinput > /dev/null"});
};
