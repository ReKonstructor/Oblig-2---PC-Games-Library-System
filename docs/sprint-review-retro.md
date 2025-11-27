# Sprint Review & Retrospective

## Sprint Review
**Date:** October 6, 2025
**Attendees:** Thisath Ovin, Halvard Mjelde

### Demonstrated Features
1. ✅ Add games manually to library
2. ✅ Mark/unmark games as favorites
3. ✅ Filter games by genre
4. ✅ View all games and favorite games
5. ✅ Remove games from library
6. ✅ Persistent storage using JSON

### Completed User Stories
- **Story #1:** Track favorite games - DONE
- **Story #6:** Categorize by genre - DONE  
- **Simplified Story #4:** Add games manually - DONE

### What Was Not Completed
- Automatic import from Steam/Epic (too complex for MVP)
- Direct game launching
- Rating/review system

## Sprint Retrospective
**Date:** October 6, 2025

### What Went Well?
- Clear division of work between team members
- Test-driven development helped catch bugs early
- Simple JSON storage worked well for MVP
- Good communication between team members

### What Could Be Improved?
- Could have started actual coding earlier
- Initial GameLibrary needed refactoring to work with Game class
- Should have planned the integration better

### Lessons Learned
- Keep MVP scope small and focused
- Integration between components needs early planning
- Unit tests are valuable for catching issues

### Action Items for Next Sprint
- Add GUI using Tkinter
- Implement actual API integration
- Add more robust error handling


## Sprint 3 Review & Retrospective

**Date:** November 26, 2025
**Attendees:** Thisath Ovin, Halvard Mjelde

### Sprint 3 Review

#### Demonstrated Features
1. ✅ Flask route tests with pytest
2. ✅ Improved error messages for Steam import
3. ✅ Code documentation with docstrings
4. ✅ Confirmation dialogs on destructive actions
5. ✅ Better input validation

#### Completed User Stories
- **Technical Story:** Flask route testing - DONE
- **User Story:** Enhanced error handling - DONE
- **Technical Story:** Code documentation - DONE

#### What Was Not Completed
- CI/CD pipeline (too complex for timeframe)
- User authentication (out of MVP scope)

### Sprint 3 Retrospective

#### What Went Well?
- Flask route tests cover main functionality
- Error messages are now user-friendly
- Code is better documented for future maintenance
- All MVP features working reliably
- Good test coverage across model and route layers

#### What Could Be Improved?
- Could have added more edge case tests
- Should have implemented logging system
- Could have added more UI polish
- No actual user testing conducted

#### Lessons Learned
- Testing Flask routes is straightforward with test client
- Good error messages improve user experience significantly
- Documentation while coding is easier than adding it later
- Three sprints provided good iterative improvement

#### Action Items for Future Projects
- Implement testing from Sprint 1
- Add logging infrastructure early
- Conduct simple user testing each sprint
- Balance AI usage with manual learning
- Document architecture decisions as ADRs