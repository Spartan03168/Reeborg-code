def homework():
    def harvest_1():
        def turn_right_custom():
            turn_left()
            turn_left()
            turn_left()

        def invert_orientation():
            turn_left()
            turn_left()

        def sequencial_movement(cycles):
            for i in range(cycles):
                move()

        move()
        for i in range(4):
            sequencial_movement(6)
            turn_left()
            move()
            turn_left()
            sequencial_movement(6)
            turn_right_custom()
            move()
            turn_right_custom()

        for j in range(4):
            sequencial_movement(6)
            turn_right_custom()
            move()
            turn_right_custom()
            sequencial_movement(6)
            turn_left()
            move()
            turn_left()

    def harvest_2():
        def turn_right_custom():
            turn_left()
            turn_left()
            turn_left()

        def invert_orientation():
            turn_left()
            turn_left()

        def sequencial_movement(cycles):
            for i in range(cycles):
                move()

        move()
        for i in range(4):
            sequencial_movement(6)
            turn_left()
            move()
            turn_left()
            sequencial_movement(6)
            turn_right_custom()
            move()
            turn_right_custom()

        for j in range(4):
            sequencial_movement(6)
            turn_right_custom()
            move()
            turn_right_custom()
            sequencial_movement(6)
            turn_left()
            move()
            turn_left()

    def harvest_3():
        def turn_right_custom():
            turn_left()
            turn_left()
            turn_left()

        def invert_orientation():
            turn_left()
            turn_left()

        def sequencial_movement(cycles):
            for i in range(cycles):
                move()

        move()
        for i in range(4):
            sequencial_movement(7)
            turn_left()
            move()
            turn_left()
            sequencial_movement(7)
            turn_right_custom()
            move()
            turn_right_custom()

        for j in range(4):
            sequencial_movement(7)
            turn_right_custom()
            move()
            turn_right_custom()
            sequencial_movement(7)
            turn_left()
            move()
            turn_left()

    def hurdle_1():
        def turn_right_custom():
            turn_left()
            turn_left()
            turn_left()

        def invert_orientation():
            turn_left()
            turn_left()

        def sequencial_movement(cycles):
            for i in range(cycles):
                move()

        move()
        for i in range(5):
            turn_left()
            move()
            turn_right_custom()
            move()
            turn_right_custom()
            move()
            turn_left()
            move()
        turn_left()
        move()
        turn_right_custom()
        move()
        turn_right_custom()
        move()

    def newspaper_0():
        def turn_right_custom():
            turn_left()
            turn_left()
            turn_left()

        def invert_orientation():
            turn_left()
            turn_left()

        def sequencial_movement(cycles):
            for i in range(cycles):
                move()

        turn_left()
        move()
        turn_right_custom()
        for i in range(2):
            sequencial_movement(2)
            turn_left()
            move()
            turn_right_custom()
        sequencial_movement(2)

        def newspaper_1():
            def turn_right_custom():
                turn_left()
                turn_left()
                turn_left()

            def invert_orientation():
                turn_left()
                turn_left()

            def sequencial_movement(cycles):
                for i in range(cycles):
                    move()

            turn_left()
            move()
            turn_right_custom()
            for i in range(2):
                sequencial_movement(2)
                turn_left()
                move()
                turn_right_custom()
            sequencial_movement(2)

        def rain_0():
            def turn_right_custom():
                turn_left()
                turn_left()
                turn_left()

            def invert_orientation():
                turn_left()
                turn_left()

            def sequencial_movement(cycles):
                for i in range(cycles):
                    move()

            move()
            invert_orientation()
            build_wall()
            invert_orientation()

            sequencial_movement(5)
            build_wall()
            invert_orientation()
            sequencial_movement(5)

        def rain_1():
            def turn_right_custom():
                turn_left()
                turn_left()
                turn_left()

            def invert_orientation():
                turn_left()
                turn_left()

            def sequencial_movement(cycles):
                for i in range(cycles):
                    move()

            def wall_constructor():
                build_wall()
                invert_orientation()

            move()
            invert_orientation()
            wall_constructor()

            turn_left()
            sequencial_movement(2)

            turn_right_custom()
            sequencial_movement(2)
            turn_left()
            wall_constructor()
            turn_left()

            sequencial_movement(3)
            turn_left()
            wall_constructor()
            turn_left()

            move()
            turn_right_custom()
            move()
            turn_left()
            wall_constructor()
            turn_left()

            sequencial_movement(3)
            turn_right_custom()
            sequencial_movement(3)
            turn_left()
            wall_constructor()
            turn_left()

            sequencial_movement(2)
            turn_left()
            wall_constructor()
            turn_left()

            move()
            turn_right_custom()
            sequencial_movement(2)
            turn_left()
            wall_constructor()

        def rain_2():
            def turn_right_custom():
                turn_left()
                turn_left()
                turn_left()

            def invert_orientation():
                turn_left()
                turn_left()

            def sequencial_movement(cycles):
                for i in range(cycles):
                    move()

            def wall_constructor():
                build_wall()
                invert_orientation()

            sequencial_movement(4)
            turn_left()
            sequencial_movement(2)
            wall_constructor()
            sequencial_movement(2)
            sequencial_movement(2)
            wall_constructor()
            sequencial_movement(2)

            turn_right_custom()
            sequencial_movement(7)
            wall_constructor()
            sequencial_movement(2)

            turn_right_custom()
            sequencial_movement(3)
            wall_constructor()
            sequencial_movement(3)

            sequencial_movement(3)
            turn_right_custom()
            move()
            turn_left()
            wall_constructor()

            sequencial_movement(3)
            turn_left()
            sequencial_movement(5)

        def token_4():
            def turn_right_custom():
                turn_left()
                turn_left()
                turn_left()

            def invert_orientation():
                turn_left()
                turn_left()

            def sequencial_movement(cycles):
                for i in range(cycles):
                    move()

            def wall_constructor():
                build_wall()
                invert_orientation()

            def token_collector():
                take()
                move()

            def planter():
                put()
                put()
                put()
                put()
                put()

            for i in range(4):
                token_collector()
            take()
            move()
            planter()
            move()


        def token_1():
            def turn_right_custom():
                turn_left()
                turn_left()
                turn_left()

            def invert_orientation():
                turn_left()
                turn_left()

            def sequencial_movement(cycles):
                for i in range(cycles):
                    move()

            def wall_constructor():
                build_wall()
                invert_orientation()

            def token_collector():
                take()
                move()

            def planter():
                put()
                put()
                put()
                put()
                put()

                sequencial_movement(4)
                token_collector()
                put()
                move()

            def token_2():
                def turn_right_custom():
                    turn_left()
                    turn_left()
                    turn_left()

                def invert_orientation():
                    turn_left()
                    turn_left()

                def sequencial_movement(cycles):
                    for i in range(cycles):
                        move()

                def wall_constructor():
                    build_wall()
                    invert_orientation()

                def token_collector():
                    take()
                    move()

                def planter():
                    put()
                    put()
                    put()
                    put()
                    put()

                    sequencial_movement(4)
                    token_collector()
                    put()
                    sequencial_movement(3)

            def token_5():
                def turn_right_custom():
                    turn_left()
                    turn_left()
                    turn_left()

                def invert_orientation():
                    turn_left()
                    turn_left()

                def sequencial_movement(cycles):
                    for i in range(cycles):
                        move()

                def wall_constructor():
                    build_wall()
                    invert_orientation()

                def token_collector():
                    take()
                    move()

                def planter(n):
                    for i in range(n):
                        put()

                sequencial_movement(2)
                for i in range(4):
                    token_collector()
                planter(4)
                sequencial_movement(2)