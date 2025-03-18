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
  CircularProgress,
  Alert,
  Chip,
} from '@mui/material';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

const CourseList = () => {
  const { user } = useAuth();
  const [courses, setCourses] = useState([]);
  const [enrollments, setEnrollments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchData();
  }, [user.id]);

  const fetchData = async () => {
    try {
      const [coursesRes, enrollmentsRes] = await Promise.all([
        axios.get('/api/courses'),
        axios.get(`/api/students/${user.id}/enrollments`)
      ]);

      setCourses(coursesRes.data);
      setEnrollments(enrollmentsRes.data);
    } catch (err) {
      setError('Failed to load courses');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleEnroll = async (courseId) => {
    try {
      await axios.post('/api/enrollments', { courseId });
      fetchData();
    } catch (err) {
      setError('Failed to enroll in course');
      console.error(err);
    }
  };

  const handleUnenroll = async (courseId) => {
    try {
      const enrollment = enrollments.find(e => e.id === courseId);
      if (enrollment) {
        await axios.delete(`/api/enrollments/${enrollment.id}`);
        fetchData();
      }
    } catch (err) {
      setError('Failed to unenroll from course');
      console.error(err);
    }
  };

  const isEnrolled = (courseId) => {
    return enrollments.some(course => course.id === courseId);
  };

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
        Available Courses
      </Typography>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      <Grid container spacing={3}>
        {courses.map((course) => (
          <Grid item xs={12} sm={6} md={4} key={course.id}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  {course.title}
                </Typography>
                <Typography variant="body2" color="textSecondary" gutterBottom>
                  Instructor: {course.instructor}
                </Typography>
                <Typography variant="body2" paragraph>
                  {course.description}
                </Typography>
                {isEnrolled(course.id) && (
                  <Chip
                    label="Enrolled"
                    color="primary"
                    size="small"
                    sx={{ mb: 1 }}
                  />
                )}
              </CardContent>
              <CardActions>
                <Button
                  size="small"
                  color="primary"
                  component={RouterLink}
                  to={`/courses/${course.id}`}
                >
                  View Details
                </Button>
                {isEnrolled(course.id) ? (
                  <Button
                    size="small"
                    color="error"
                    onClick={() => handleUnenroll(course.id)}
                  >
                    Unenroll
                  </Button>
                ) : (
                  <Button
                    size="small"
                    color="primary"
                    onClick={() => handleEnroll(course.id)}
                  >
                    Enroll
                  </Button>
                )}
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default CourseList; 