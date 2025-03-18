import { useState, useEffect } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Typography,
  Grid,
  Card,
  CardContent,
  CardActions,
  Button,
  List,
  ListItem,
  ListItemText,
  Divider,
  CircularProgress,
  Alert,
} from '@mui/material';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

const StudentDashboard = () => {
  const { user } = useAuth();
  const [enrollments, setEnrollments] = useState([]);
  const [assignments, setAssignments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [enrollmentsRes, assignmentsRes] = await Promise.all([
          axios.get(`/api/students/${user.id}/enrollments`),
          axios.get(`/api/students/${user.id}/assignments`)
        ]);

        setEnrollments(enrollmentsRes.data);
        setAssignments(assignmentsRes.data);
      } catch (err) {
        setError('Failed to load dashboard data');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [user.id]);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="200px">
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Welcome, {user.name}!
      </Typography>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      <Grid container spacing={3}>
        {/* Enrolled Courses */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Your Courses
              </Typography>
              {enrollments.length === 0 ? (
                <Typography color="textSecondary">
                  You are not enrolled in any courses yet.
                </Typography>
              ) : (
                <List>
                  {enrollments.map((course) => (
                    <div key={course.id}>
                      <ListItem>
                        <ListItemText
                          primary={course.title}
                          secondary={course.instructor}
                        />
                        <Button
                          component={RouterLink}
                          to={`/courses/${course.id}`}
                          size="small"
                          color="primary"
                        >
                          View Details
                        </Button>
                      </ListItem>
                      <Divider />
                    </div>
                  ))}
                </List>
              )}
            </CardContent>
            <CardActions>
              <Button
                component={RouterLink}
                to="/courses"
                size="small"
                color="primary"
              >
                Browse All Courses
              </Button>
            </CardActions>
          </Card>
        </Grid>

        {/* Upcoming Assignments */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Upcoming Assignments
              </Typography>
              {assignments.length === 0 ? (
                <Typography color="textSecondary">
                  No upcoming assignments.
                </Typography>
              ) : (
                <List>
                  {assignments.map((assignment) => (
                    <div key={assignment.id}>
                      <ListItem>
                        <ListItemText
                          primary={assignment.title}
                          secondary={`Due: ${new Date(assignment.dueDate).toLocaleDateString()} - ${assignment.courseName}`}
                        />
                      </ListItem>
                      <Divider />
                    </div>
                  ))}
                </List>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default StudentDashboard; 