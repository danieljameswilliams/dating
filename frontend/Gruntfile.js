module.exports = function ( grunt ) {
    // Project configuration.
    grunt.initConfig({
        // Metadata.
        pkg: grunt.file.readJSON('package.json'),
        banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - ' +
            '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
            '<%= pkg.homepage ? "* " + pkg.homepage + "\\n" : "" %>' +
            '* Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>;' +
            ' Licensed <%= _.pluck(pkg.licenses, "type").join(", ") %> */\n',
        // Task configuration.
        sass: {
            dist: {
                options: {
                    style: 'compressed',
                    update: true
                },
                files: {
                    'public/stylesheets/main.css': 'public/scss/main.scss'
                }
            }
        },
        autoprefixer: {
            dist: {
                options: {
                  browsers: ['last 8 versions']
                },
                files: {
                    'public/stylesheets/main.css': 'public/stylesheets/main.css'
                }
            }
        },
        concat: {
            options: {
                separator: ';'
            },
            dist: {
                src: [
                    // Libraries
                    'public/javascripts/lib/jquery.js',
                    'public/javascripts/lib/handlebars.js',

                     // Partials
                    'public/javascripts/partials/*.js',

                    // Main App
                    'public/javascripts/main.js'
                ],
                dest: 'public/javascripts/main-min.js'
            }
        },
        watch: {
            css: {
                files: 'public/scss/**/*.scss',
                tasks: ['sass', 'autoprefixer']
            },
            js: {
                files: [ 'public/javascripts/main.js', 'public/javascripts/lib/*.js', 'public/javascripts/partials/*.js' ],
                tasks: ['concat']
            }
        }
    });

    // These plugins provide necessary tasks.
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-autoprefixer');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task.
    grunt.registerTask('css', ['sass', 'autoprefixer']);
    grunt.registerTask('js', ['concat']);
    grunt.registerTask('default', ['css', 'js']);
};
